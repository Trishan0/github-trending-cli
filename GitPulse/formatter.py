from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

console = Console()


def format_number(num):
    """Format large numbers (1000 -> 1k, 1000000 -> 1M)"""
    if num >= 1_000_000:
        return f"{num/1_000_000:.1f}M"
    elif num >= 1_000:
        return f"{num/1_000:.1f}k"
    return str(num)


def format_repos(repos: list, language: str = None):
    """
    Display repository information using rich formatting.
    """
    if not repos:
        console.print(
            "[yellow]⚠️  No repositories found for the given criteria.[/yellow]"
        )
        return

    # Header
    title = Text("🔥 GitHub Trending Repositories", style="bold magenta")
    console.print(Panel(title, border_style="bright_blue"))
    console.print(f"[cyan]Found {len(repos)} repositories[/cyan]\n")

    # Create table
    table = Table(show_header=True, header_style="bold cyan", border_style="blue")
    table.add_column("Rank", style="dim", width=6)
    table.add_column("Repository", style="bold green")
    table.add_column("Language", style="yellow")
    table.add_column("⭐ Stars", justify="right", style="bright_yellow")
    table.add_column("🍴 Forks", justify="right", style="bright_blue")
    table.add_column("Description", style="white", max_width=50)

    # Add rows
    for idx, repo in enumerate(repos, 1):
        table.add_row(
            str(idx),
            repo["name"],
            repo.get("language") or "N/A",
            format_number(repo["stargazers_count"]),
            format_number(repo["forks_count"]),
            repo.get("description", "No description")[:100] or "No description",
        )

    console.print(table)

    # Footer with URLs
    console.print(
        "\n[dim]💡 Tip: Visit repositories at https://github.com/owner/repo[/dim]"
    )
