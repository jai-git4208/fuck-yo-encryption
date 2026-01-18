# Contributing (Read this, you illiterate f*ck)

So you want to contribute to `fuck-yo-encryption`? Bold choice. We assume you're here because you either hate standard encryption libraries or you just like seeing the word "FUCK" in your terminal. Either way, welcome.

## The Rules 

1.  **Don't be boring.** If your PR makes the code boring, I will close it.
2.  **Code must actually work.** Just because the output looks like garbage doesn't mean the code should be garbage.
3.  **Tests or GTFO.** If you break the drilled-down encryption logic, you're dead to me.
4.  **Keep the attitude.** This library has a personality. Don't sanitize it.

## How to Set Up (If you can't figure this out, give up)

Clone the repo, obviously. Then:

```bash

python -m venv venv
source venv/bin/activate  # Windows users: figure it out yourself :3

pip install -e .
```

## Running Tests

We use `pytest`. If you don't know what that is, google it.

```bash
pip install pytest
pytest
```

If the tests fail, **do not** open a PR. Fix them.

## Pull Requests

- **Title**: Make it descriptive. "Fix" is not descriptive. "Fix: Stopped the infinite loop of FUCKs" is better.
- **Description**: Tell me what you did and why. If you added a feature, explain why I should care.
- **Attitude**: Optional but encouraged.

## Reporting Bugs

If you find a bug, congrats. You broke something that was already barely holding it together. Open an issue, but:
- Include the traceback.
- Tell me what you were doing.
- Don't just say "it doesn't work".

## License

By contributing, you agree that your code becomes part of this glorious mess under the MIT license. Now get to work :3.
