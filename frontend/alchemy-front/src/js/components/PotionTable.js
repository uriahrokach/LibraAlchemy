import React from 'react';

import '../../css/Table.css'


const PotionTable = (props) => {
    return (
        <div className='table-wrapper'>
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
                            <td>{potion.effects.join(', ')}</td>
                            <td>{potion.description}</td>
                            <td><button>⋮</button></td>
                        </tr>
                    )
                })}
            </table>
        </div>
    )
}

export default PotionTable