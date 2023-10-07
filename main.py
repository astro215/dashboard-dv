import streamlit as st

def main():
    st.title("Embedded Power BI Report")

    # Embed the Power BI report using an iframe
    st.components.v1.html(
        """
        <div id="embedContainer"></div>
        <script src="embed_powerbi.js"></script>
        """,
        height=600,  # Set the desired height
        width=800,   # Set the desired width
        scrolling=True,
    )

if __name__ == "__main__":
    main()
