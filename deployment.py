
from prefect import flow

if __name__ == "__main__":
    flow.from_source(
        source="https://github.com/PratikWayase/ScalableML-Pipeline.git",
        entrypoint="main.py:ml_workflow",
    ).deploy(
        name="first-prefect-deployment",
        work_pool_name="DC-work-pool",
        tags=["dev"],
        job_variables={"pip_packages": ["pandas", "skops", "scikit-learn"]},
    )
    