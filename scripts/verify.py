#!/usr/bin/env python3
"""Validate package files and exercise documented installs in temporary homes."""
from pathlib import Path
import re
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    '.gitignore', 'LICENSE', 'README.md', 'docs/codex.md',
    'docs/claude-code.md', 'prompts/agent-wait-guidance.md',
    'skills/agent-wait-guidance/SKILL.md', 'templates/codex-AGENTS.md',
    'templates/claude-CLAUDE.md', 'scripts/verify.py',
}


def check(condition, message):
    if not condition:
        raise AssertionError(message)
    print('PASS:', message)


def main():
    actual = {str(p.relative_to(ROOT)) for p in ROOT.rglob('*')
              if p.is_file() and '.git' not in p.relative_to(ROOT).parts
              and '__pycache__' not in p.relative_to(ROOT).parts}
    check(actual == EXPECTED, 'exact package file set')
    skill = (ROOT / 'skills/agent-wait-guidance/SKILL.md').read_text()
    check(skill.startswith('---\n'), 'frontmatter starts at first byte')
    _, frontmatter, body = skill.split('---\n', 2)
    check('name: agent-wait-guidance\n' in frontmatter, 'skill name')
    check('description: Use when [AGENT_WAIT_GUIDANCE] appears. Show wait card.\n'
          in frontmatter, 'original skill trigger')
    check(bool(body.strip()), 'nonempty skill body')
    check('예상: 30초 이상 · 최대: 산정 불가' in body, 'uncertain ETA fallback')
    hook = (ROOT / 'prompts/agent-wait-guidance.md').read_text()
    check(hook.startswith('[AGENT_WAIT_GUIDANCE]\n'), 'hook marker')
    for template in ('codex-AGENTS.md', 'claude-CLAUDE.md'):
        text = (ROOT / 'templates' / template).read_text()
        check(hook in text, template + ' contains unmodified hook')
        check('including both 예상 and 최대' in text,
              template + ' loads detailed maximum-time rule')
    for path in ROOT.rglob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            if link.startswith(('https://', 'http://', '#', 'mailto:')):
                continue
            check((path.parent / link.split('#')[0]).exists(),
                  str(path.relative_to(ROOT)) + ' link: ' + link)
    import os
    for doc, folder in [('codex.md', '.agents'), ('claude-code.md', '.claude')]:
        text = (ROOT / 'docs' / doc).read_text()
        candidates = re.findall(r'```bash\n(.*?)\n```', text, re.S)
        install = next(block for block in candidates if 'dest=' in block)
        syntax = subprocess.run(['bash', '-n'], input=install, text=True,
                                capture_output=True)
        check(syntax.returncode == 0, doc + ' install shell syntax')
        with tempfile.TemporaryDirectory(prefix='focusbong-install-') as home:
            env = dict(os.environ, HOME=home)
            first = subprocess.run(['bash', '-c', install], cwd=ROOT,
                                   env=env, text=True, capture_output=True)
            check(first.returncode == 0, doc + ' fresh install')
            dest = Path(home) / folder / 'skills/agent-wait-guidance/SKILL.md'
            source = ROOT / 'skills/agent-wait-guidance/SKILL.md'
            check(dest.read_bytes() == source.read_bytes(),
                  doc + ' byte-identical installed skill')
            dest.write_text('existing personal modification\n')
            second = subprocess.run(['bash', '-c', install], cwd=ROOT,
                                    env=env, text=True, capture_output=True)
            check(second.returncode != 0, doc + ' existing install refusal')
            check(dest.read_text() == 'existing personal modification\n',
                  doc + ' preserves existing modification')
    print('Package checks complete. This does not test live model behavior.')


if __name__ == '__main__':
    main()
