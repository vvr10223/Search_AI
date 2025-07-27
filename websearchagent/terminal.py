from webgraph import webagent
import argparse

from termcolor import colored
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text




def main():
    parser = argparse.ArgumentParser(description="Web Search Agent Terminal")
    parser.add_argument("query", type=str, help="Search query")
    args = parser.parse_args()

    query = args.query
    print(colored("🔍 Searching...", "yellow"))

    try:
        console = Console()

        response = webagent(query)
        print(response)
        #console.print("\n[bold green]Search Query:[/bold green]", query)
        console.print(colored(response,"white"))

        print("\n" + colored("✔ Search Completed", "green"))

    except Exception as e:
        print(colored(f"❌ Error: {e}", "red"))

if __name__ == "__main__":
    main()
