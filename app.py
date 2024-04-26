# 웹상에 띄우고 싶으면 해당 디렉토리로 가서, streamlit run app.py 라고 치면 된다.

import streamlit as st

print("page reloaded")

st.set_page_config(
    page_title="포켓몬 도감",
    page_icon='./images/icons1.png'
)
st.markdown("""
<style>
img {
    max-height: 300px;
}
.streamlit_expanderContent div {
    display: flex; 
    justify-content: center;
}
</style>     
""", unsafe_allow_html=True)

st.title("Streamlit 포켓몬 도감")
st.subheader("제2장")
st.markdown("**포켓몬**그녀석! :sunglasses:")
st.text("포켓몬을 하나씩 추가해서 도감을 채워보세요")

type_dict = {
    "노말" : "○",
    "격투" : "★",
    "비행" : "§",
    "독" : "♠",
    "땅" : "■",
    "바위" : "◆",
    "벌레" : "＆",
    "고스트" : "＠",
    "강철" : "□",
    "불꽃" : "△",
    "물" : "▽",
    "풀" : "◁",
    "전기" : chr(0x1F60A),
    "에스퍼" : "♧",
    "얼음" : "▣",
    "드래곤" : "※",
    "악" : "♤",
    "페어리" : "♥"        
}

initial_pokemons = [
    {
         "name" : "피카츄",
         "type" : ["전기"],
         "image_url" : "https://i.namu.wiki/i/Ap102Lu877se-VfMgsHjoZm_yQM3T0VH98oamQfgNBZbfit87wE2T5uWNsCheHVSsWp--Y_Ke9rMKQVzW-76QGyk3qy0Ie17mFNEgF9xXo_8qwW3s_Mlpqc7dEQQ3nayrvlRpjfJYbqeOCg6LU5uNw.webp"
    },
    {
         "name" : "누오",
         "type" : ["물","땅"],
         "image_url" : "https://i.namu.wiki/i/ETC92zJAFoGjTIFQORB0N0mb3yaV_yJfxWnvC0qX2kcZC8NGGIoE19Yv9xe6bBRv-PYK9RjF9mBCFp_HSJMBYWHpraG1pO5AcrF_6svTzD9ESp_mgwnV0dqRtMTZBrjTFm1FS-oKiSczHrOk4LTu2A.webp"
    },    
    {
         "name" : "갸라도스",
         "type" : ["물","비행"],
         "image_url" : "https://i.namu.wiki/i/0ZovfA8eM20H5JvBwhJMhR7WgtfnQvj8DkJRq9sx-507L4xI8GSIdjHM6xmvd7_X4BcgTGVobgXMSy0pKNRxcOmkSA93t-UEcVB41og8ZOtXpQibRN2K9ACgkFTBHd34tSYBes8Fsk4NnjrYY-BOFA.webp"
    },     
    {
         "name" : "개굴닌자",
         "type" : ["물","악"],
         "image_url" : "https://i.namu.wiki/i/Yn2IiVM5fmNZ3sq-ZtQODFPjb47grWSX_3N7bPkl55N9VuirpCRt_E0wcHnF8GuoSYsngi9drRxqlTNq3ilyt6LwDx95oHHB4m4HVBHVz9bSqIYIqctvCUBmp3tb38ajrQB92zAXzuzsMP-pU01Wtg.webp"
    },     
    {
         "name" : "루카리오",
         "type" : ["격투","강철"],
         "image_url" : "https://i.namu.wiki/i/9OnNa2HQ6NTuFsTo8z4ucS90-R87nyFv1Ifkrw3eNg1Ky2ZKq282JmYt0w40zYdzAm2wriElq08C6QQtlUYVWW7ffn4M0yte98rPsrN7yRJwVNexuuWF4QPtO2QQW7jX4G2NZEdfDSLgHdpL2MhOpQ.webp"
    },  
    {
         "name" : "에이스번",
         "type" : ["불꽃"],
         "image_url" : "https://i.namu.wiki/i/zUJslpgaSJBfF2uZ4EPCZhckhGJ6AfRCJyEBSop65r_y7CRqEkhG3Var8_IiA7mXU1PgPk3vcnjZIXuKCRi6EZmNtoBdSke7m7kcpvhsGJ8NKIXsK9lNh3amnLffWmuBZLltLtrG2wVvkqa7UTxeVg.webp"
    },  
]

example_pokemon = {
    "name" : "알로라 디그다",
    "type" : ["땅","강철"],
    "image_url" : "https://i.namu.wiki/i/dcs_AAnMLrJ21vyCELL3-F4-36UM6qLypl77lP4jHZN-_gC8xT9PMYEcFWTv-m0U3ZaUm-TRe-S8PTgjfrkn2Bg5NoJvsdMKkrvf9GHQmS7o89juQXjYCa6ekM-08iL2WE9i0T09Cv8h0VYDesrrDg.webp"
}

if "pokemons" not in st.session_state :
    st.session_state.pokemons = initial_pokemons

auto_complete = st.toggle("예시 데이터로 채우기")
with st.form(key="form"):
    col1, col2 = st.columns(2)
    with col1 :
        name = st.text_input(label="포켓몬 이름", 
                             value=example_pokemon["name"] if auto_complete else "")
    with col2 :
        types = st.multiselect(
            label="포켓몬 속성",
            options=list(type_dict.keys()),
            max_selections=2,
            default=example_pokemon["type"] if auto_complete else []
        )
    image_url = st.text_input(
        label = "포켓몬 이미지 url",
        value = example_pokemon["image_url"] if auto_complete else ""
    )
    submit = st.form_submit_button(label="Submit")
    if submit :
        if not name:
            st.error("포켓몬의 이름이 빠져 있어요")
        elif len(types) == 0:
            st.error("포켓몬의 속성이 하나도 없어요")
        else :
            st.success("포켓몬을 추가합니다.")
            st.session_state.pokemons.append({
                "name" : name,
                "type" : types,
                "image_url" : image_url if image_url else "./images/pokemon3.png"
            })
            
    
with st.form(key="form2"):
    st.text("메롱")
    submit2 = st.form_submit_button(label="Submit")

for i in range(0, len(st.session_state.pokemons), 3):
    row_pokemons = st.session_state.pokemons[i:i+3]
    cols = st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            num_name =  pokemon["name"] + str(i+j+1)
            with st.expander(label = num_name, expanded=True):
                st.image(pokemon["image_url"])
                emoji = [ str(type_dict[x]) for x in pokemon["type"] ]
                st.text(" / ".join(pokemon["type"]))
                st.subheader(" / ".join(emoji))
                delete_button = st.button(label="삭제", key=i+j, use_container_width=True)
                if delete_button :
                    print("delete button clicked")
                    del st.session_state.pokemons[i+j]
                    st.rerun()
    
