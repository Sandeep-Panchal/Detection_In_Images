# import required packages, libraries and files
import streamlit as st
import detection_file as det_file

# UI starts from here
st.write('# Detection...')

# creating a sidebar with various options
operation = ['Home', 'Face Detection', 'Eyes Detection', 'Emotion Detection']
selected = st.sidebar.selectbox(label='Choose one of the following...', options=operation, key='key_1')

if selected == 'Home':
    st.write('## Home')
    st.write('This is a app wherein users can upload the image and get the face, eyes, emotion detected based on the selected option from the sidebar.')
    st.write('Please select one of the options from the left sidebar.')

elif selected == 'Face Detection':
    st.write('## {}'.format(selected))
    st.write('Please upload an image. It will detect eyes and draw box around the detected face.')
    cascade_file = '../haar-cascade-files-master/haarcascade_frontalface_default.xml'

elif selected == 'Eyes Detection':
    st.write('## {}'.format(selected))
    st.write('Please upload an image. It will detect eyes and draw boxes around the detected eyes.')
    cascade_file = '../haar-cascade-files-master/haarcascade_eye.xml'

# elif selected == 'Emotion Detection':
    # st.write('## {}'.format(selected))
    # st.write('Please upload an image. It will detect emotion of a human.')
    # cascade_file = '../haar-cascade-files-master/haarcascade_frontalface_default'
    # st.warning('Emotion Detection is under maintainence... Please stay tuned for the update on this...')

# displays upload image option only if the page is not Home page
if selected != 'Home':
    uploaded_img = st.file_uploader('Upload an Image', type=['png', 'jpg', 'jpeg'])

# calling the function process_uploaded_image from detection_file
# then based on selected options, we will call face detection or eyes detection or other function
if selected != 'Home' and selected != 'Emotion Detection':
    if uploaded_img is not None:
        img_process = det_file.process_uploaded_image(uploaded_img)

        if selected == 'Face Detection':
            det_file.face_detection(img_process, cascade_file)
        elif selected == 'Eyes Detection':
            det_file.eyes_detection(img_process, cascade_file)

elif selected == 'Emotion Detection':
    st.warning('Emotion Detection is under maintainence... Please stay tuned for the update on this...')

