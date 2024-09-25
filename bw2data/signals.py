from blinker import signal

project_changed = signal(
    "bw2data.project_changed",
    doc="""
Emitted when project changed, after redirecting any SQLite database references.

Expected inputs:
    * `bw2data.projects.ProjectDataset` instance

No expected return value.
""",
)

project_created = signal(
    "bw2data.project_created",
    doc="""
Emitted when project created, but before switching to that project, and before any filesystem ops.

Expected inputs:
    * `bw2data.projects.ProjectDataset` instance

No expected return value.
""",
)

activity_saved = signal(
    "bw2data.activity_saved",
    doc="""
Emitted when an ActivityDataset has been saved.

Expected inputs:
    * `bw2data.backends.schema.ActivityDataset` instance

No expected return value.
""",
)

exchange_saved  = signal(
    "bw2data.exchange_saved",
    doc="""
    Emitted when an ExchangeDataset has been saved.

    Expected inputs:
        * `bw2data.backends.schema.ExchangeDataset` instance

    No expected return value.
    """,
)

database_written  = signal(
    "bw2data.database_written",
    doc="""
    Emitted when a (SQLite) database has been written.

    Expected inputs:
        * `dict` of the form::
            {
                ('database name', 'dataset code'): {dataset}
            }

    No expected return value.
    """,
)