"""Writing functions"""

__author__ = "730648018"


def mimic(message: str) -> str:
    """Mimic the given message"""
    return message


def main() -> None:
    """Main function- print mimic"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
