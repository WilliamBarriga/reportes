const url = 'http://127.0.0.1:8000';


function getRegions(){
    return fetch(`${url}/api/scrap-region`)
        .then(res => res.json())
        .then(res => res.data)

}

export default {
    getRegions
}
