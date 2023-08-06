# *******************************************************
# Nom ......... : Editeur métadonnes exif d'image
# Rôle ........ : edite les métadonnées de l'image afficher
# Auteur ...... : bahsine et liubov
# Version ..... : V0.1 du 29/07/2023
# Licence ..... : réalisé dans le cadre du cours d'outils collaboratifs
# (../..)
# Compilation : pas de compilation
# Usage : demarrer le programme a l'aide de la commande streamlit ru edit_meta.py
#********************************************************

#importer la classe Image from la bibliotheque exif
from exif import Image
#importer la bibliotheque streamlit
import streamlit as st




#demarrer notre application à l'aide d'un titre
st.title("Bienvenue dans notre application qui vous permet d'editer  le metadata d'une image ")
#afficher l'image sur laquelle on va travaillé
image = st.image("monument.jpg")
#demarrer un formulaire
with st.form(key='formulaire'):
    #créer les champs de saisie pour chaque parametres de l'image  avec une valeur par default
    color_space = st.text_input('color_space :', value=65535)
    compressed_bits_per_pixel = st.text_input('compressed_bits_per_pixel :', value=4.0)
    compression = st.text_input('compression :', value=6)
    contrast = st.text_input('contrast :', value=1)
    custom_rendered = st.text_input('custom_rendered :', value=0)
    datetime_original = st.text_input('datetime_original :', value='2003:11:23 18: 07:37')
    digital_zoom_ratio = st.text_input('digital_zoom_ratio :', value=1.0)
    exposure_bias_value = st.text_input('exposure_bias_value :', value=0.0)
    exposure_mode = st.text_input('exposure_mode :', value=0)
    exposure_program = st.text_input('exposure_program :', value=3)
    exposure_time = st.text_input('exposure_time :', value=0.008)
    f_number = st.text_input('f_number :', value=4.5)
    file_source = st.text_input('file_source :', value=None)


    focal_length = st.text_input('focal_length :', value=23.33)
    focal_length_in_35mm_film = st.text_input('focal_length_in_35mm_film :', value=35)


    light_source = st.text_input('light_source :', value=0)
    make = st.text_input('make :', value='NIKONCORPORATION')
    max_aperture_value = st.text_input('max_aperture_value :', value=3.0)
    metering_mode = st.text_input('metering_mode :', value=3)
    model = st.text_input('model :', value='NIKOND2H')
    orientation = st.text_input('orientation :', value=1)

    resolution_unit = st.text_input('resolution_unit :', value=2)
    saturation = st.text_input('saturation :', value=0)
    scene_capture_type = st.text_input('scene_capture_type :', value=0)
    sensing_method = st.text_input('sensing_method :', value=2)
    sharpness = st.text_input('sharpness :', value=0)
    subject_distance_range = st.text_input('subject_distance_range :', value=0)
    subsec_time = st.text_input('subsec_time :', value=63)
    subsec_time_digitized = st.text_input('subsec_time_digitized :', value=63)
    subsec_time_original = st.text_input('subsec_time_original :', value=63)

    white_balance = st.text_input('white_balance :', value=0)
    x_resolution = st.text_input('x_resolution :', value=256.0)
    y_resolution = st.text_input('y_resolution :', value=256.0)

    #crée un boutton pour soumettre le formulaire
    submit_button = st.form_submit_button(label="Editer")

#si l'utilisateur appuie sur le boutton
if submit_button :
    #on creer le chemin vers l'image
    img_filename = 'monument.jpg'
    img_path = f'{img_filename}'

    #on ouvre l'image en mode lecture binaire  et la transforme en classe Image
    with open(img_path, 'rb') as img_file:
        img = Image(img_file)

    #essayé ce script sinon renvoie l'exception
    try :
        #on affecte  a chaque attribut de la classe img  la valeur entré par l'utilisateur
        img.color_space = color_space
        img.compressed_bits_per_pixel = compressed_bits_per_pixel
        img.compression = compression
        img.contrast = contrast
        img.custom_rendered = custom_rendered
        img.datetime_original = datetime_original
        img.digital_zoom_ratio = digital_zoom_ratio

        img.exposure_bias_value = exposure_bias_value
        img.exposure_mode = exposure_mode
        img.exposure_program = exposure_program
        img.exposure_time = exposure_time
        img.f_number = f_number


        img.focal_length = focal_length
        img.focal_length_in_35mm_film = focal_length_in_35mm_film


        img.light_source = light_source
        img.make = make
        img.max_aperture_value = max_aperture_value
        img.metering_mode = metering_mode
        img.model = model
        img.orientation = orientation

        img.resolution_unit = resolution_unit
        img.saturation = saturation
        img.scene_capture_type = scene_capture_type

        img.sensing_method = sensing_method
        img.sharpness = sharpness
        img.subject_distance_range = subject_distance_range
        img.subsec_time = subsec_time
        img.subsec_time_digitized = subsec_time_digitized
        img.subsec_time_original = subsec_time_original
        img.white_balance = white_balance
        img.x_resolution = x_resolution
        img.y_resolution = y_resolution

        #on commence la suvegarde des données saisie
        with open(f'{img_filename}', 'wb') as image_save: #ouvrir en mode ecriture binaire
                image_save.write(img.get_file()) #on recupere les données ecrit precedement et on les enregistre
        #retourner un message de confirmation
        st.write("Vos Modifications en été bien enregistré",)
    #sinon si on a pas réeussie
    except :
        #on renvoie un message d'erreur
        st.write("Vous avez eu un erreur dans les modifications")

