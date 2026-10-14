import typer

from rich import print
from rich.panel import Panel

app = typer.Typer()


data = {
    "name": "Rick",
    "age": 42,
    "items": [{"name": "Portal Gun"}, {"name": "Plumbus"}],
    "active": True,
    "affiliation": None,
}

@app.command()
def data_print():
    print(Panel.fit(str(data), title="Test Title"))

@app.command()
def hello(name: str):
    print(f"[bold red]Hello {name}[/bold red]")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


def entrypoint():
    app()