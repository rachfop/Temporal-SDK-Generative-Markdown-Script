# Generate Stats

Generate statictcs of the Temporal documentation's How-to's.

## Temporal SDK

The [Temporal SDK documentation](https://docs.temporal.io/application-development) should follow a set of standards when creating documentation for coding languages. The purpose of this script is to remove the barrier of entry when creating SDK documentation by automating repetitive tasks.

## Installation

Install python3:

```bash
brew install python
```

Install the requirements

```python
pip -r requirements.txt
```

## Usage

Run the following command:

```python
python3 generate-stats.py
```

Preview or save the generated file.

Results: You have successfully generated the a chart displaying stats on Temporal's documentation.

## To update the list of required files

The file `topic-list.txt` contains a list of required files. To update this file:

- add a comma to the end of the next to last item: `,`
- add the file name in single quotes: `'`
- use the following format:

`'how-to-spawn-a-workflow-execution-in-go'`

## License

[MIT](https://choosealicense.com/licenses/mit/)
