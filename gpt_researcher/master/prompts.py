from datetime import datetime


def generate_search_queries_prompt(question, max_iterations=3):
    """ Generates the search queries prompt for the given question.
    Args: question (str): The question to generate the search queries prompt for
    Returns: str: The search queries prompt for the given question
    """

    return f"Scrivi {max_iterations} query di ricerca di Google per cercare online che formano un'opinione oggettiva a partire da: \"{question}\"" \
           f"Usa la data corrente se necessario: {datetime.now().strftime('%d %B %Y')}.\n" \
           f"Devi rispondere con una lista di stringhe nel seguente formato: [\"query 1\", \"query 2\", \"query 3\"]."


def generate_report_prompt(question, context, report_format="apa", total_words=1000):
    """ Generates the report prompt for the given question and research summary.
    Args: question (str): The question to generate the report prompt for
            research_summary (str): The research summary to generate the report prompt for
    Returns: str: The report prompt for the given question and research summary
    """

    return f'Informazioni: """{context}"""\n\n' \
           f'Usando le informazioni sopra, rispondi alla seguente' \
           f' domanda o compito: "{question}" in un report dettagliato --' \
           " Il report deve focalizzarsi sulla risposta alla domanda, deve essere ben strutturato, informativo," \
           f" approfondito e completo, con dati e cifre se disponibili e un minimo di {total_words} parole.\n" \
           "Dovresti sforzarti di scrivere il report più lungo possibile usando tutte le informazioni rilevanti e necessarie.\n" \
           "Dovresti scrivere il report utilizzando la sintassi markdown.\n " \
           f"Usa un tono imparziale e giornalistico. \n" \
           "DEVI formare la tua opinione concreta e valida basata sulle informazioni date. NON deviare a conclusioni generiche e prive di significato.\n" \
           f"DEVI scrivere tutti gli URL delle fonti utilizzate alla fine del report come riferimenti e assicurati di non aggiungere fonti duplicate, ma solo un riferimento per ciascuna.\n" \
           f"DEVI scrivere il report nel formato {report_format}.\n " \
            f"Cita i risultati delle ricerche utilizzando annotazioni nel testo. Cita solo i risultati più \
            rilevanti che rispondano accuratamente alla domanda. Posiziona queste citazioni alla fine \
            della frase o del paragrafo che le citano.\n"\
            f"Fai del tuo meglio, questo è molto importante per la mia carriera. " \
            f"Ipotesi che la data corrente sia {datetime.now().strftime('%d %B %Y')}"


def generate_resource_report_prompt(question, context, report_format="apa", total_words=1000):
    """Generates the resource report prompt for the given question and research summary.

    Args:
        question (str): The question to generate the resource report prompt for.
        context (str): The research summary to generate the resource report prompt for.

    Returns:
        str: The resource report prompt for the given question and research summary.
    """
    return f'"""{context}"""\n\nSulla base delle informazioni sopra, genera un rapporto di raccomandazione bibliografica per la seguente' \
           f' domanda o argomento: "{question}". Il rapporto dovrebbe fornire un\'analisi dettagliata di ogni risorsa raccomandata,' \
           'spiegando come ogni fonte possa contribuire a trovare risposte alla domanda di ricerca.\n' \
           'Concentrati sulla rilevanza, affidabilità e importanza di ogni fonte.\n' \
           'Assicurati che il rapporto sia ben strutturato, informativo, approfondito e segua la sintassi Markdown.\n' \
           'Include fatti, cifre e numeri rilevanti quando disponibili.\n' \
           'Il rapporto dovrebbe avere una lunghezza minima di 700 parole.\n' \
           'DEVI includere tutti gli URL delle fonti rilevanti.'

def generate_custom_report_prompt(query_prompt, context, report_format="apa", total_words=1000):
    return f'"{context}"\n\n{query_prompt}'


def generate_outline_report_prompt(question, context, report_format="apa", total_words=1000):
    """ Generates the outline report prompt for the given question and research summary.
    Args: question (str): The question to generate the outline report prompt for
            research_summary (str): The research summary to generate the outline report prompt for
    Returns: str: The outline report prompt for the given question and research summary
    """

    return f'"""{context}""" Utilizzando le informazioni sopra riportate, genera un sommario per un report di ricerca utilizzando la sintassi Markdown' \
           f' per la seguente domanda o argomento: "{question}". Il sommario dovrebbe fornire una struttura ben organizzata' \
           ' per il report di ricerca, incluse le sezioni principali, le sottosezioni e i punti chiave da trattare.' \
           ' Il report di ricerca dovrebbe essere dettagliato, informativo, approfondito e di un minimo di 1.200 parole.' \
           ' Usa la sintassi Markdown appropriata per formattare il sommario e garantire la leggibilità.'



def get_report_by_type(report_type):
    report_type_mapping = {
        'research_report': generate_report_prompt,
        'resource_report': generate_resource_report_prompt,
        'outline_report': generate_outline_report_prompt,
        'custom_report': generate_custom_report_prompt
    }
    return report_type_mapping[report_type]


def auto_agent_instructions():
   return """
        Questo compito coinvolge la ricerca su un argomento fornito, a prescindere dalla sua complessità o dalla disponibilità di una risposta definitiva. La ricerca è condotta da un server specifico, definito dal suo tipo e ruolo, con ogni server che richiede istruzioni distinte.
        Agente
        Il server è determinato dall'ambito dell'argomento e dal nome specifico del server che potrebbe essere utilizzato per ricercare l'argomento fornito. Gli agenti sono categorizzati in base alla loro area di competenza, e ogni tipo di server è associato a un corrispondente emoji.

        esempi:
        compito: "dovrei investire in azioni Apple?"
        risposta: 
        {
            "server": "💰 Agente Finanziario",
            "agent_role_prompt": "Sei un assistente AI analista finanziario esperto. Il tuo obiettivo principale è redigere rapporti finanziari comprensivi, perspicaci, imparziali e metodicamente strutturati basati sui dati forniti e sulle tendenze di mercato."
        }
        compito: "potrebbe essere redditizio il commercio di scarpe da ginnastica?"
        risposta: 
        { 
            "server": "📈 Agente Analista di Business",
            "agent_role_prompt": "Sei un assistente AI analista di affari esperto. Il tuo obiettivo principale è produrre rapporti di affari comprensivi, perspicaci, imparziali e sistematicamente strutturati basati sui dati di affari forniti, sulle tendenze di mercato e sull'analisi strategica."
        }
        compito: "quali sono i siti più interessanti a Tel Aviv?"
        risposta:
        {
            "server": "🌍 Agente di Viaggio",
            "agent_role_prompt": "Sei un assistente AI guida turistica con esperienza di viaggio nel mondo. Il tuo scopo principale è redigere rapporti di viaggio coinvolgenti, perspicaci, imparziali e ben strutturati sulle località fornite, inclusa la storia, le attrazioni e gli spunti culturali."
        }
    """


def generate_summary_prompt(query, data):
    """ Generates the summary prompt for the given question and text.
    Args: question (str): The question to generate the summary prompt for
            text (str): The text to generate the summary prompt for
    Returns: str: The summary prompt for the given question and text
    """

    return f'{data}\n Utilizzando il testo sopra, riassumilo in base al seguente compito o quesito: "{query}".\n Se il ' \
       f'quesito non può essere risposto utilizzando il testo, DEVI riassumere brevemente il testo.\n Includi tutte le ' \
       f'informazioni fattuali come numeri, statistiche, citazioni, ecc. se disponibili. '


