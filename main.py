from services.fda_client import FDAClient
from services.recall_checker import RecallChecker
from services.ai_translator import AITranslator
from storage.history import SearchHistory

client = FDAClient()
checker = RecallChecker()
translator = AITranslator()
history = SearchHistory()

name = input("Enter Drug Name: ").strip()

med = client.fetch_drug_info(name)

if med is None:
    print("Drug not found or invalid input!")
else:
    med.display_info()

    text = f"""
    Usage:
    {med.usage}

    Warnings:
    {med.warnings}

    Side Effects:
    {med.side_effects}

    Instructions:
    {med.instructions}
    """

    simple = translator.simplify_text(text)
    print(simple)

    recall = checker.check_recall(name)

    if recall:
        print("\n⚠ WARNING: This drug has recall notices!")
        print(f"Reason: {recall['reason']}")
        print(f"Status: {recall['status']}")
        print(f"Date: {recall['date']}")

    if simple:
        history.save_search(
            med.name,
            simple
        )