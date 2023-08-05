from exif import Image
import streamlit as st


st.title("Bienvenue dans notre application qui vous permet d'editer  le metadata d'une image ")
image = st.image("stonehenge.jpg")
with st.form(key='formulaire'):
    make = st.text_input('make :', value='NIKON CORPORATION')
    model = st.text_input('model :', value='NIKON D3000')
    x_resolution = st.text_input('x_resolution :', value='240.0')
    y_resolution = st.text_input('y_resolution :', value='240.0')
    resolution_unit = st.text_input('resolution_unit :', value='2')
    software = st.text_input('software :', value='Adobe Photoshop Lightroom Classic 11.3 (Macintosh)')
    datetime = st.text_input('datetime :', value='2022:04:30 14:29:51')
    artist = st.text_input('artist :', value='Matthew Gove')
    copyright = st.text_input('copyright :', value='Copyright 2022 Matthew Gove. All Rights Reserved.')
    _exif_ifd_pointer = st.text_input('_exif_ifd_pointer :', value='316')
    exposure_time = st.text_input('exposure_time :', value='0.003125')
    f_number = st.text_input('f_number :', value='9.0')
    exposure_program = st.text_input('exposure_program :', value='2')
    photographic_sensitivity = st.text_input('photographic_sensitivity :', value='200')
    exif_version = st.text_input('exif_version :', value='0231')
    datetime_original = st.text_input('datetime_original :', value='2022:02:16 21:36:08')
    datetime_digitized = st.text_input('datetime_digitized :', value='2022:02:16 21:36:08')
    offset_time = st.text_input('offset_time :', value='-04:00')
    shutter_speed_value = st.text_input('shutter_speed_value :', value='8.321928')
    aperture_value = st.text_input('aperture_value :', value='6.33985')
    exposure_bias_value = st.text_input('exposure_bias_value :', value='0.0')
    max_aperture_value = st.text_input('max_aperture_value :', value='3.6')
    metering_mode = st.text_input('metering_mode :', value='5')
    light_source = st.text_input('light_source :', value='0')
    flash = st.text_input('flash :', value='Flash(flash_fired=False')
    focal_length = st.text_input('focal_length :', value='18.0')
    subsec_time_original = st.text_input('subsec_time_original :', value='50')
    subsec_time_digitized = st.text_input('subsec_time_digitized :', value='50')
    color_space = st.text_input('color_space :', value='1')
    sensing_method = st.text_input('sensing_method :', value='2')
    file_source = st.text_input('file_source :', value='3')
    scene_type = st.text_input('scene_type :', value='1')
    cfa_pattern = st.text_input('cfa_pattern :', value='None')
    custom_rendered = st.text_input('custom_rendered :', value='0')
    exposure_mode = st.text_input('exposure_mode :', value='0')
    white_balance = st.text_input('white_balance :', value='0')
    digital_zoom_ratio = st.text_input('digital_zoom_ratio :', value='1.0')
    focal_length_in_35mm_film = st.text_input('focal_length_in_35mm_film :', value='27')
    scene_capture_type = st.text_input('scene_capture_type :', value='0')
    gain_control = st.text_input('gain_control :', value='0')
    contrast = st.text_input('contrast :', value='0')
    saturation = st.text_input('saturation :', value='0')
    sharpness = st.text_input('sharpness :', value='0')
    subject_distance_range = st.text_input('subject_distance_range :', value='0')
    body_serial_number = st.text_input('body_serial_number :', value='3254465')
    lens_specification = st.text_input('lens_specification :', value='(18.0, 55.0, 3.5, 5.6)')
    lens_model = st.text_input('lens_model :', value='18.0-55.0 mm f/3.5-5.6')
    submit_button = st.form_submit_button(label="submit")
if submit_button :
    img_filename = 'stonehenge.jpg'
    img_path = f'{img_filename}'

    with open(img_path, 'rb') as img_file:
        img = Image(img_file)

    try:
        img.make = make
        img.model = model
        img.x_resolution = x_resolution
        img.y_resolution = y_resolution
        img.resolution_unit = resolution_unit
        img.software = software
        img.datetime = datetime
        img.artist = artist
        img.copyright = copyright
        img.exposure_time = exposure_time
        img.f_number = f_number
        img.exposure_program = exposure_program
        img.photographic_sensitivity = photographic_sensitivity
        img.datetime_original = datetime_original
        img.datetime_digitized = datetime_digitized
        img.offset_time = offset_time
        img.shutter_speed_value = shutter_speed_value
        img.aperture_value = aperture_value
        img.exposure_bias_value = exposure_bias_value
        img.max_aperture_value = max_aperture_value
        img.metering_mode = metering_mode
        img.light_source = light_source

        img.focal_length = focal_length
        img.subsec_time_original = subsec_time_original
        img.subsec_time_digitized = subsec_time_digitized
        img.color_space = color_space
        img.sensing_method = sensing_method
        img.file_source = file_source
        img.scene_type = scene_type

        img.custom_rendered = custom_rendered
        img.exposure_mode = exposure_mode
        img.white_balance = white_balance
        img.digital_zoom_ratio = digital_zoom_ratio
        img.focal_length_in_35mm_film = focal_length_in_35mm_film
        img.scene_capture_type = scene_capture_type
        img.gain_control = gain_control
        img.contrast = contrast
        img.saturation = saturation
        img.sharpness = sharpness
        img.subject_distance_range = subject_distance_range
        img.body_serial_number = body_serial_number
        img.lens_model = lens_model

        with open(f'{img_filename}', 'wb') as image_save:
            image_save.write(img.get_file())
        st.write("Vos Modifications en été bien enregistré",)
    except :
        print("vous avez un erreur de saisie ")




