# aw-importer-savemytime

This is a small [importer](https://docs.activitywatch.net/en/latest/importers.html) script for the time tracking app [SaveMyTime](https://savemytime.co/).
Using the pro version of SaveMyTime, one can export a csv file with all tracked data, which this script then imports into [ActivityWatch](https://activitywatch.net/).

> **Note:** While this script shouldn't break anything (apart from maybe overwriting data previously imported into the *savemytime* bucket), it's not quite done, either.
> The events won't look great in the [web UI](https://github.com/ActivityWatch/aw-webui/).


## Usage
1. Install the dependencies
2. Export a csv file of the desired date range, rename it to [`smt_export.csv`](smt_export.csv) and put it in the same directory as the [`main.py`](main.py) file.
3. Execute the [`main.py`](main.py) file.


## Dependencies
- [aw-client](https://github.com/ActivityWatch/aw-client)
- [pandas](https://pandas.pydata.org/docs/getting_started/install.html)


## TODOs
- [ ] As of now, there isn't really a suitable `event_type` for time tracking data like this.
  - maybe *[currentwindow](https://docs.activitywatch.net/en/latest/buckets-and-events.html#currentwindow)*?
    - also requires an AFK bucket
    - **or**: prefix with *aw-watcher-android* (see [here](https://github.com/ActivityWatch/aw-webui/blob/8b0c63550ef2c8fccf896375ac11f64685e467de/src/store/modules/buckets.js#L33-L37))
- [ ] The handling of an already-existing bucket is more or less untested.
- [ ] SaveMyTime's categories are not imported. This is by design, since ActivityWatch has [its own notion of categories](https://docs.activitywatch.net/en/latest/features/categorization.html), but can be easily changed.
