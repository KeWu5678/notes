# Git hooks

Tracked hooks for this vault. Enable them once per clone:

```sh
git config core.hooksPath .githooks
```

## `prepare-commit-msg`

At commit time, drafts a commit-message body that summarizes your **staged**
changes, grouped by top-level folder (e.g. `Engineering`, `Math`), using the
`claude` CLI. The draft is pre-filled into your editor — you always review and
edit before the commit is finalized.

- Skips merges, squashes, and amends.
- Skips when nothing is staged.
- If `claude` is missing, times out (~45s), or errors, it falls back to a plain
  per-folder file list, so a commit is never blocked.

To disable: `git config --unset core.hooksPath`.
