# here

The goal of the `here` package is to enable easy file referencing in project-oriented workflows. `here` uses the top-level directory of a project, as identified by the presence of a `pyproject.toml` file, to easily build paths to files.

This package is inspired by the [R package of the same name](https://here.r-lib.org/).

## Installation
Install the released version of here from CRAN:

```
pip install here
```

## Usage

The here package creates paths relative to the top-level directory. The package displays the top-level of the current project on load or any time you call here():

```
from here import here

here()
here("path/to/file.txt")
```

You can build a path relative to the top-level directory in order to read or write a file:

```
here("data/penguins.csv")

import pandas as pd

# ...

df.write_csv(here("data/penguins.csv"))
```

These relative paths work regardless of where the associated source file lives inside your project, like analysis projects with data and reports in different subdirectories.