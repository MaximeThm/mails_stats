import mailbox
import pandas as pd
from collections import Counter

# Remplacez 'votre_fichier.mbox' par le chemin de votre fichier MBOX
MBOX_FILE = "mails.mbox"

def analyze_emails(mbox_file):
    # Ouvrir le fichier MBOX
    mbox = mailbox.mbox(mbox_file)
    dates = []

    # Parcourir tous les emails pour extraire les dates
    for message in mbox:
        if 'date' in message:
            # Extraire la date et la formater
            date = pd.to_datetime(message['date'], errors='coerce')
            if pd.notnull(date):
                dates.append(date.date())  # Conserver uniquement la date (sans l'heure)

    # Compter le nombre d'emails par jour
    date_counts = Counter(dates)

    # Convertir les données en DataFrame pour analyse
    df = pd.DataFrame(date_counts.items(), columns=["Date", "Number of emails"])
    df = df.sort_values("Date")

    # Afficher les résultats
    df.to_csv("statistiques_emails.csv", index=False)
    print("Results have been exported in csv format")

# Exécuter l'analyse
analyze_emails(MBOX_FILE)

