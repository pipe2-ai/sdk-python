# pipe2

Official Python SDK for [Pipe2.ai](https://pipe2.ai) — run AI media pipelines
(video generation, image generation, text-to-speech, video reframing) and track
their results.

Async, fully typed with Pydantic models.

## Install

```bash
pip install pipe2
```

Requires Python 3.10+.

## Authenticate

`Pipe2Client` takes a bearer token — a personal access token from your
[Pipe2.ai account](https://pipe2.ai), or a user JWT. It defaults to the
production endpoint `https://api.pipe2.ai/v1/graphql`.

```python
from pipe2 import Pipe2Client

client = Pipe2Client(token=os.environ["PIPE2_TOKEN"])
```

## Run a pipeline

Pipeline inputs vary per pipeline, so they are passed as a dict. Browse the
catalog and each pipeline's inputs at [pipe2.ai](https://pipe2.ai).

```python
import asyncio, os
from pipe2 import Pipe2Client


async def main():
    client = Pipe2Client(token=os.environ["PIPE2_TOKEN"])

    run = await client.run_pipeline(
        pipeline_slug="video-generator",
        input={"prompt": "a red fox in falling snow, cinematic"},
    )
    print("run:", run.run_pipeline.run_id)

    # Runs are asynchronous — fetch the current status by run id, and repeat
    # until it reaches a terminal state.
    status = await client.get_pipeline_run(id=run.run_pipeline.run_id)
    print("status:", status.pipeline_runs_by_pk.status)


asyncio.run(main())
```

## Estimate cost before running

Runs are billed in credits. `estimate_pipeline_cost` returns the price for a
given pipeline and input without starting anything.

```python
estimate = await client.estimate_pipeline_cost(
    pipeline_slug="video-generator",
    input={"prompt": "a red fox in falling snow"},
)
```

## Browse pipelines

```python
pipelines = await client.get_pipelines()
```

## Related

- [Pipe2.ai](https://pipe2.ai) — pipeline catalog, pricing, and docs
- [pipe2-cli](https://github.com/pipe2-ai/pipe2-cli) — agent-native command line tool
- [sdk-go](https://github.com/pipe2-ai/sdk-go) — Go client

## License

Apache-2.0
