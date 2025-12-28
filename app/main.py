from app.database import init_db, seed_initial_data
from app.cli import run_cli


def main():
    init_db()
    seed_initial_data()
    run_cli()


if __name__ == "__main__":
    main()
