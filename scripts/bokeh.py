import marimo

__generated_with = "0.14.10"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    from skimage import io
    from pathlib import Path
    return io, mo


@app.cell
def _(io, mo):
    files = [
        "fireworks_1.jpg",
        "cherry-blossom_1.jpg",
        "tennoz-isle.jpg"
    ]

    def get_image_list() -> list[str]:
      return [file.split(".")[0] for file in files]

    def get_image(image_name: str):
      img_file = [file for file in files if file.split(".")[0] == image_name][0]
      path = mo.notebook_location() / "public" / "dataset" / img_file
      return io.imread(path)

    return get_image, get_image_list


@app.cell
def _(get_image_list, mo):
    image_dropdown = mo.ui.dropdown(
        get_image_list(), value="fireworks_1", label="target image"
    )
    return (image_dropdown,)


@app.cell
def _(get_image, image_dropdown, mo):
    image = get_image(image_dropdown.value)
    image_preview = mo.image(
        src=image,
        height="200px",
        rounded=True,
        caption="target (reference)",
    )

    mo.hstack(justify="start", align="start", items=[image_dropdown, image_preview])
    return


if __name__ == "__main__":
    app.run()
