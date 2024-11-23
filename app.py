import streamlit as st
import pandas as pd
from datetime import datetime
import base64

def create_download_link(file_path):
    with open(file_path, "rb") as f:
        bytes_data = f.read()
    b64 = base64.b64encode(bytes_data).decode()
    return f'<a href="data:application/pdf;base64,{b64}" download>PDF herunterladen</a>'

def main():
    # Konfiguration der Seite
    st.set_page_config(
        page_title="Unternehmens-News Dashboard",
        page_icon="📰",
        layout="wide"
    )

    # Sidebar für Navigation und Filterung
    st.sidebar.title("Navigation")
    
    # Mock-Login (zur Demonstration)
    st.sidebar.markdown("---")
    st.sidebar.markdown("👤 Angemeldet als: Max Mustermann")
    st.sidebar.markdown("🏢 Abteilung: Marketing")

    # Hauptbereich
    st.title("📰 Unternehmens-News Dashboard")

    # Tabs für verschiedene Ansichten
    tab1, tab2 = st.tabs(["Aktueller Newsticker", "Archiv"])

    with tab1:
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("PDF-Ansicht")
            uploaded_file = st.file_uploader(
                "PDF hochladen (nur für Administratoren)", 
                type="pdf"
            )
            if uploaded_file is not None:
                st.success("PDF erfolgreich hochgeladen!")
                st.markdown("PDF-Vorschau wird hier angezeigt")
                
        with col2:
            st.subheader("KI-Zusammenfassung")
            summary = st.text_area(
                "Zusammenfassung bearbeiten (nur für Administratoren)",
                value="""Wichtigste Updates dieser Woche:
- Neue Vertriebsaktion gestartet
- Team-Event am 15.12.
- Produktupdate Version 2.4 live
                """,
                height=200
            )

    with tab2:
        # Archiv-Funktionalität
        st.subheader("News-Archiv")
        
        # Filter-Optionen
        col1, col2 = st.columns([1, 1])
        with col1:
            selected_month = st.selectbox(
                "Monat auswählen",
                ["November 2024", "Oktober 2024", "September 2024"]
            )
        with col2:
            search_term = st.text_input("Suche im Archiv")

        # Demo-Daten für Archiv
        archive_data = pd.DataFrame({
            'Datum': ['2024-11-16', '2024-11-09', '2024-11-02'],
            'KW': ['KW 46', 'KW 45', 'KW 44'],
            'Zusammenfassung': [
                'Vertriebsaktion Q4, Team-Events, Produktupdate',
                'Quartalsabschluss, Neue Marketingkampagne',
                'Mitarbeiter des Monats, IT-Updates'
            ]
        })
        
        # Anzeige der Archiv-Einträge
        for _, row in archive_data.iterrows():
            with st.expander(f"{row['KW']} - {row['Datum']}"):
                st.write(row['Zusammenfassung'])
                st.markdown("🔍 [PDF anzeigen](#)")

if __name__ == "__main__":
    main()
