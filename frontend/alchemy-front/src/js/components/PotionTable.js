import { useState } from 'react';
import { PotionDeleter, EffectTag} from './PotionComponents';

import '../../css/Table.css'
import '../../css/PotionComps.css'
import {ReactComponent as TrashIcon} from '../../icons/trash.svg';


const PotionTable = (props) => {
    const [deletePotion, setPotion] = useState(null);
    return (
        <div className='table-wrapper'>
            {deletePotion && <PotionDeleter potion={deletePotion} setPotion={setPotion} /> }
            <table className='table'>
                <tr>
                    <th>שיקוי</th>
                    <th>השפעות</th>
                    <th>תיאור</th>
                    <th></th>
                </tr>
                {props.potions && props.potions.map(potion => {
                    return (
                        <tr>
                            <td>{potion.name}</td>
                            <td>{potion.effects.map((effect) => <EffectTag effect={effect}/>)}</td>
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