import os

language = input("Enter the name of the coding language:").strip()
if not os.path.exists(language):
    os.makedirs(language)


def cap_last_word(self):
    return " ".join(self.capitalize().split()[:-1]) + " " + self.split()[-1].title()


with open(f"{language.lower()}/index.md", "w") as index:
    index.write(
        f"""---
id: index
title: {language.capitalize()} SDK
---
- [Getting started](overview)\n"""
    )

topic_list = open("topic-list.txt").read().split(",")
topic_list.sort()
counter = 2
for topic in topic_list:
    renamed_topic = (
        str(topic).replace("go", language).replace("'", "").replace(" ", "").strip()
    )
    capped_last_word = cap_last_word(renamed_topic.replace("-", " "))
    counter += 1
    sidebar_id = (
        topic.replace("-", " ")
        .replace("in go", "")
        .replace("go", "")
        .replace("how to", "")
        .strip("'")
        .strip("' ")
    )
    with open(f"{language.lower()}/{renamed_topic.lower()}.md", "a") as the_file:
        the_file.write(
            f"""---
id: {renamed_topic.lower()}
title: {capped_last_word}
sidebar_label: {sidebar_id.replace("'", "").strip().capitalize()}
sidebar_postiong: {counter}
description: {sidebar_id.replace("'", "").strip().capitalize()}\n"""
        )
        the_file.write(
            f"""tags:
    - developer-guide
    - sdk
    - {language}
---\n"""
        )

    with open(f"{language.lower()}/index.md", "a") as index:
        index.write(f"""- [{capped_last_word}]({renamed_topic.lower()})\n""")

with open(f"{language.lower()}/overview.md", "w") as index:
    index.write(
        f"""---
id: overview
title: How to use the Temporal {language.capitalize().strip()} SDK
sidebar_label: Temporal {language.capitalize()} SDK
description: Add the Temporal {language.capitalize()} SDK to your project.
tags:
    - developer-guide
    - sdk
    - {language}
---\n"""
    )
    index.write(
        f"""\nThe Temporal {language.capitalize()} SDK provides a framework for Temporal Application development in the {language.capitalize()} language.
The SDK contains the following tools:

- A Temporal Client to communicate with a Temporal Cluster
- APIs to use within your Workflows
- APIs to create and manage Worker Entities and Worker Processes

### Get the SDK

Add the [Temporal {language.capitalize()} SDK](https://github.com/temporalio/sdk-{language.lower()}) to your project:

```bash
ENTER TERMINAL SCRIPT
```

Or clone the {language.capitalize()} SDK repo to your preferred location:

```bash
git clone git@github.com:temporalio/sdk-{language}.git
```

### Are there executable code samples?

You can find a complete list of executable code samples in the [samples library](/docs/samples-library/#{language}), which includes Temporal {language.capitalize()} SDK code samples from the [temporalio/samples-{language}](https://github.com/temporalio/samples-{language}) repo.
Additionally, each of the {language.capitalize()} SDK Tutorials is backed by a fully executable template application.

### Where is the {language.capitalize()} SDK technical reference?

The [Temporal {language.capitalize()} SDK API reference](URL_INPUT) is published on [INPUT](URL_INPUT).
"""
    )
