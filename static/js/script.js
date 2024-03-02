servidor = "http://127.0.0.1:5000"
rota = "/adm"
//rota_anime = "/novo_anime"
//rota_capitulo = "/novo_capitulo"


url_anime = servidor+rota;
//url_capitulo = servidor+rota+rota_capitulo;
console.log(url_anime)

botao = document.getElementById('button_anime');
botao.addEventListener('click',function () {

    nome_anime = document.getElementById('nome_anime').value
    logo_anime = document.getElementById('logo_anime').value
    trailer_anime = document.getElementById('trailer_anime').value
    descricao = document.getElementById('descricao').value
    
    Anime = {'tipoCadastro':'Anime','nome_anime':nome_anime,'logo_anime':logo_anime,'trailer_anime':trailer_anime,'descricao':descricao}
    
    axios.post(url_anime, Anime)
    .then(function(response){
    console.log(response.data);

    })
    .catch(function (error) {
    // manipula erros da requisição
    console.error(error);
  })
})


//page anime
function troca_ep_info_trailer(tipo){
    console.log(tipo)
    const ep = document.getElementById("ep");
    const ep_click = document.getElementById("ep_click");
    const desc = document.getElementById("desc");
    const desc_click = document.getElementById("desc_click");
    const trai = document.getElementById("trai");
    const trai_click = document.getElementById("trai_click");

    const episodios = document.getElementById("episodios");
    const descricao = document.getElementById("descricao");
    const trailer = document.getElementById("trailer");

    if (tipo =="ep") {
        episodios.style.display = "block";
        descricao.style.display = "none";
        trailer.style.display = "none";

        ep.id = "ep_click";
        if (desc == null){
            desc_click.id = "desc";
        } else if (trai == null){
            trai_click.id = "trai";
        } else if (desc_click == null) {
            desc.id = desc.id;
        } else {
            trai.id = trai.id
        }
    } else if(tipo =="desc") {
        descricao.style.display = "block";
        episodios.style.display = "none";
        trailer.style.display = "none";

        desc.id = "desc_click";
        if (ep == null){
            ep_click.id = "ep";
        } else if (trai == null){
            trai_click.id = "trai";
        } else if (ep_click == null) {
            ep.id = ep.id;
        } else {
            trai.id = trai.id
        }
    } else if (tipo == "trai") {
        trailer.style.display = "block";
        episodios.style.display = "none";
        descricao.style.display = "none";

        trai.id = "trai_click";
        if (desc == null){
            desc_click.id = "desc";
        } else if (ep == null){
            ep_click.id = "ep";
        } else if (desc_click == null) {
            desc.id = desc.id;
        } else {
            ep.id = ep.id
        }
    }
}