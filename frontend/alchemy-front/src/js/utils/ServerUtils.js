import axios from 'axios'


const ENDPOINT = '/api';

const authenticate =  {
    username: process.env.REACT_APP_USERNAME,
    password: process.env.REACT_APP_PASSWORD
}

const getMaterials = async () => {
    const response = await axios.get(`${ENDPOINT}/materials`, {auth: authenticate})
    return response.data;
}

const getTechnics = async () => {
    const response = await axios.get(`${ENDPOINT}/technics`, {auth: authenticate})
    return response.data;
}

const brewPotions = async (materials, technic) => {
    const response = await axios.post(`${ENDPOINT}/brew`, {         
        materials: materials,
        technic: technic,
    }, {auth: authenticate});
    return response.data;
}

const createPotion = async (potionName, materials, technic, description) => {
    const response = await axios.put(`${ENDPOINT}/potion`, {
        name: potionName,
        materials: materials,
        technic: technic,
        description: description,
    }, {auth: authenticate})
    return response.data;
}

const getEffects = async (materials, technic) => {
    const response = await axios.post(`${ENDPOINT}/effect/ingredients`, {         
        materials: materials,
        technic: technic,
    }, {auth: authenticate});
    return response.data;
}

const getPotionByName = async (name) => {
    const response = await axios.get(`${ENDPOINT}/potion/${name}`, {auth: authenticate})
    return response.data;
}

const deletePotion = async (name) => {
    const response = await axios.delete(`${ENDPOINT}/potion/${name}`, {auth: authenticate})
    return response.data;
}


const getPotionRegex = async (regex) => {
    const response = await axios.get(`${ENDPOINT}/potion?regex=${regex}`, {auth: authenticate})
    return response.data;
}

const getEffectByName = async (name) => {
    const response = await axios.get(`${ENDPOINT}/effect?effect=${name}`, {auth: authenticate})
    return response.data;
}


export {getMaterials, getTechnics, brewPotions, createPotion, deletePotion, getPotionRegex, getPotionByName, getEffects, getEffectByName};