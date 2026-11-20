# Python Foundations

My hands-on Python foundations for a path into ML/AI engineering.
Each module has graded exercises with their own tests, reviewed like code in a pull request.

## How to run

Requires [uv](https://docs.astral.sh/uv/) and Python 3.14.

```bash
git clone git@github.com:hilton-eng/python-foundations.git
cd python-foundations
uv sync
for f in exercises/m1_1/ex*.py; do uv run python "$f"; done
```

Each file prints `all tests passed` when its tests succeed.

## Repo layout

```
exercises/m1_1/   # Module 1.1 exercises, one file per exercise, tests included
src/              # the python_foundations package
pyproject.toml    # project spec and dependencies
uv.lock           # exact pinned versions
```

## Module 1.1: Python core and the data model

### Lesson 1: names, references and mutability

**What I learned**
- A variable is a label on an object, not a box. `b = a` adds a second label; nothing is copied.
- Rebinding (`a = [9]`) moves one label; mutating (`a.append(9)`) changes the shared object, so every label sees it.
- Mutable defaults (`def f(x, acc=[])`) are created once and shared between calls; the fix is `acc=None`.
- Shallow vs deep copy: copy exactly what you change, for example a new dict per row rather than a deep copy of everything.
- Data-cleaning functions should return new objects and never mutate their input, and a test should prove the input is unchanged.

**Exercises**

| File | What it does |
|---|---|
| `ex1_safe_append.py` | Appends without the mutable default trap |
| `ex2_normalise_rows.py` | Cleans CSV-style rows without touching the originals |
| `ex3_make_grid.py` | Builds a grid whose rows are independent lists |
| `ex4_merge_config.py` | Merges configs so nested lists stay independent |

**Mistakes I made and fixed**
- `zip((a, b))` passes one tuple instead of two lists, so unpacking failed. Fixed to `zip(a, b)`.
- Pushed code without running it. Now I run every file before `git add`.
- A test that looped over an empty result could never fail. I now check the length first, and watch each new test fail once on purpose.
