import streamlit as st

st.title('🖼️ Youtube Image Extractor')
st.header('YouTube Thumbnail Image Extractor App')

with st.expander('About this app'):
    st.write('This app retrieves the thumbnail image from a YouTube video.')

# Image settings
st.sidebar.header('Settings')
img_dict = {'Max': 'maxresdefault', 'High': 'hqdefault', 'Medium': 'mqdefault', 'Standard': 'sddefault'}
selected_img_quality = st.sidebar.selectbox('Select image quality', ['Max', 'High', 'Medium', 'Standard'])
img_quality = img_dict[selected_img_quality]

yt_url = st.text_input('Paste YouTube URL', 'https://www.youtube.com/watch?v=f8FAJXPBdOg')


# Retrieving YouTube video ID from URL
# yt = st.experimental_get_query_params()['yt'][0]

def get_ytid(input_url):
    ytid = input_url.split('=')[-1]
    return ytid

# Display YouTube thumbnail image
if yt_url != '':
    ytid = get_ytid(yt_url)  # yt or yt_url

    yt_img = 'http://img.youtube.com/vi/{}/{}.jpg'.format(ytid,img_quality)
    st.image(yt_img)
    st.write('YouTube video thumbnail image URL: ', yt_img)
else:
    st.write('☝️ Enter URL to continue ...')