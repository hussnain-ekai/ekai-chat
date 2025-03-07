To use ekai with pipx on replit, you can run these commands in the replit shell:

```bash
pip install pipx
pipx run ekai-chat ...normal ekai args...
```

If you install ekai with pipx on replit and try and run it as just `ekai` it will crash with a missing `libstdc++.so.6` library.

