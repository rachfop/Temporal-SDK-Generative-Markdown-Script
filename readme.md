# Generate md sdk

Generate Markdown SDK is a script to generate templatized SDK markdown files for the language of your choice.

## Temporal SDK

The [Temporal SDK documentation](https://docs.temporal.io/application-development) should follow a set of standards when creating documentation for coding languages. The purpose of this script is to remove the barrier of entry when creating SDK documentation by automating repetitive tasks.

## Installation

Install python3:

```bash
brew install python
```

This script uses Python's standard library. No other installation is required.

## Usage

Run the following command:

```python
python3 generate-md-sdk.py
```

Enter the language you'd like to generate for example:

```bash
Enter the name of the coding language: python
```

Results: You have successfully generated the required markdown files for your SDK documents.

## To update the list of required files

The file `topic-list.txt` contains a list of required files. To update this file:

- add a comma to the end of the next to last item: `,`
- add the file name in single quotes: `'`
- use the following format:

`'how-to-spawn-a-workflow-execution-in-go'`

## License

[MIT](https://choosealicense.com/licenses/mit/)
