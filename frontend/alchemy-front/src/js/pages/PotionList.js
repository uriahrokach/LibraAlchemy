import React, { useState, useEffect} from 'react';
import PotionTable from '../components/PotionTable';
import { getPotionRegex } from '../utils/ServerUtils';
import { useAsync } from 'react-async-hook';
import { InputController } from '../components/SearchComponents'

const PotionList = (props) => {
    const [regex, setRegex] = useState('')
    const [potions, setPotions] = useState([])
    const asyncPotion = useAsync(getPotionRegex, [regex]);

    useEffect(() => {    
        if (asyncPotion.status === "success"){
            setPotions(asyncPotion.result);
        }
    }, [asyncPotion.result])
    return (
        <div>
            <InputController setValue={setRegex}/>
            {asyncPotion.error && `error: ${asyncPotion.error.message}, ${asyncPotion.error.data}`}
            <div>
                <PotionTable potions={potions}/>
            </div>
            {asyncPotion.loading && "loading..."}
        </div>
    )
}

export {PotionList};