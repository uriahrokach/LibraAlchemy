import axios from 'axios'

const ENDPOINT = 'http://localhost:5000';

const getMaterials = async () => {
    const response = await axios.get(`${ENDPOINT}/materials`)
    return response.data;
}

const getTechnics = async () => {
    const response = await axios.get(`${ENDPOINT}/technics`)
    return response.data;
}

const brewPotions = async (materials, technic) => {
    const response = await axios.post(`${ENDPOINT}/brew`, {         
        materials: materials,
        technic: technic
    });
    return response.data;
}

const createPotion = async (potionName, materials, technic, description) => {
    const response = await axios.put(`${ENDPOINT}/potion`, {
        name: potionName,
        materials: materials,
        technic: technic,
        description: description
    })
    return response.data;
}

const getEffects = async (materials, technic) => {
    const response = await axios.post(`${ENDPOINT}/effect/ingredients`, {         
        materials: materials,
        technic: technic
    });
    return response.data;
}

const getPotionByName = async (name) => {
    const response = await axios.get(`${ENDPOINT}/potion/${name}`)
    return response.data;
}

const deletePotion = async (name) => {
    const response = await axios.delete(`${ENDPOINT}/potion/${name}`)
    return response.data;
}


const getPotionRegex = async (regex) => {
    const response = await axios.get(`${ENDPOINT}/potion?regex=${regex}`)
    return response.data;
}

const getEffectByName = async (name) => {
    const response = await axios.get(`${ENDPOINT}/effect?effect=${name}`)
    return response.data;
}

export {getMaterials, getTechnics, brewPotions, createPotion, deletePotion, getPotionRegex, getPotionByName, getEffects, getEffectByName};