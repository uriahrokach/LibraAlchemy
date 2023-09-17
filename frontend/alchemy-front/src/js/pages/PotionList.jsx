import React, { useState, useEffect} from 'react';
import PotionTable from '../components/PotionTable';
import { ReactComponent as ExcelIcon } from '../../icons/excel.svg';
import { getPotionRegex, downloadPotionList } from '../utils/ServerUtils';
import '../../css/PotionComps.css';
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
            <div className='search-container'>
                <InputController setValue={setRegex} placeholder='שם השיקוי...'/>
                <div title="Export to Excel">
                    <ExcelIcon className="trash" onClick={() => downloadPotionList(regex)}/>
                </div>
            </div>
            {asyncPotion.error && `error: ${asyncPotion.error.response.data.detail}`}
            <div>
                {potions.length !== 0 && <PotionTable potions={potions}/>}
                {potions.length === 0 && <div style={{direction: "rtl"}}>אין שיקויים המכילים את הביטוי "{regex}"</div>}
            </div>
            {asyncPotion.loading && "loading..."}
        </div>
    )
}

export {PotionList};