import React, { useState } from 'react';
import { useAsync } from 'react-async-hook';
import { PotionDeleter, EffectTag, PotionTypeTag } from './PotionComponents';
import { getPotionTypeByPotion } from '../utils/ServerUtils';

import '../../css/Table.css'
import '../../css/PotionComps.css'
import {ReactComponent as TrashIcon} from '../../icons/trash.svg';

const PotionTypeList = (props) => {
    const potionTypes = useAsync(getPotionTypeByPotion, [props.potion.name])
    return (
        <>
            {potionTypes.loading && 'loading...'}
            {potionTypes.error && potionTypes.error.response.data.detail}
            {potionTypes.result && <>{potionTypes.result.map(potionType => <PotionTypeTag {...potionType} />)}</>}
        </>
    )
}

const PotionTable = (props) => {
    const [deletePotion, setPotion] = useState(null);
    return (
        <div className='table-wrapper'>
            {deletePotion && <PotionDeleter potion={deletePotion} setPotion={setPotion} /> }
            <table className='table'>
                <tr>
                    <th>שיקוי</th>
                    <th>השפעות</th>
                    <th>סוגים</th>
                    <th>תיאור</th>
                    <th></th>
                </tr>
                {props.potions && props.potions.map(potion => {
                    return (
                        <tr>
                            <td>{potion.name}</td>
                            <td>{potion.effects.map((effect) => <EffectTag effect={effect}/>)}</td>
                            <td><PotionTypeList potion={potion} /></td>
                            <td>{potion.description}</td>
                            <td><TrashIcon className='trash' onClick={() => setPotion(potion)}/></td>
                        </tr>
                    )
                })}
            </table>
        </div>
    )
}

export default PotionTable