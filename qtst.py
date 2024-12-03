import streamlit as st
from streamlit_authenticator import Authenticate

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,  # Sera géré automatiquement
            'logged_in': False,  # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,  # Sera géré automatiquement
            'logged_in': False,  # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "nom_du_cookie",  # Le nom du cookie, un str quelconque
    "cle_du_cookie",  # La clé du cookie, un str quelconque
    30  # Le nombre de jours avant que le cookie expire
)

# Connexion utilisateur
authenticator.login()

def accueil():
    st.title("Bienvenue sur la page d'accueil")
    st.image("https://i.gifer.com/3W7u.gif")  # Lien vers le GIF

def photos_chat():
    st.subheader("Les photos de mon chat")
    # Créer des colonnes pour afficher les images sur la même ligne
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://goodflair.com/app/uploads/2024/07/beautiful-bengal-cat-1536x1024.jpg")
    with col2:
        st.image("https://goodflair.com/app/uploads/2024/09/beautiful-bengal-cat-1536x1024.jpg")
    with col3:
        st.image("https://www.rustica.fr/images/chat-bengale-bengali-l1200-h0.jpg.webp")

if st.session_state["authentication_status"]:
    # Le bouton de déconnexion au-dessus du menu
    authenticator.logout("Déconnexion")
    
    # Menu dans la barre latérale, seulement si connecté
    option = st.sidebar.selectbox(
        "Menu",
        ["Accueil", "Les photos de mon chat"]
    )

    # Affichage du contenu selon l'option sélectionnée
    if option == "Accueil":
        accueil()
    elif option == "Les photos de mon chat":
        photos_chat()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
