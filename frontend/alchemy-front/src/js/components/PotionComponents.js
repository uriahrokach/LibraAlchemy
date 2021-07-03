import ReactDOM from 'react-dom';
import { useAsync } from 'react-async-hook';
import { toast } from 'react-toastify';
import Tippy from '@tippy.js/react';

import {deletePotion, getEffectByName } from '../utils/ServerUtils';
import '../../css/PotionComps.css';
import 'tippy.js/dist/tippy.css';
import 'tippy.js/themes/light.css'

const Modal = (props) => {
    return ReactDOM.createPortal(
        <>
            <div className='overlay' />
            <div className='potion-card'>
                    {props.children}
            </div>
        </>, document.getElementById('popup')
    )    
}

const PotionDeleter = (props) => {
    const name = props.potion ? props.potion.name : null;
    return (
        <Modal>
            <h3>האם למחוק את השיקוי {name}?</h3>
            <div>
                <button className='alert-button' onClick={async () => {
                    try{
                        const response = await deletePotion(name);
                        props.setPotion(null);
                        window.location.reload(false);
                    } catch (error) {
                        toast.error(error.response.data.detail);
                        props.setPotion(null);
                    }
                } }>מחק</button>
                <button className='normal-button' onClick={() => { props.setPotion(null) }}>ביטול</button>
            </div>
        </Modal>
    )
}

const EffectTag = (props) => {
    const effectsData = useAsync(getEffectByName, [props.effect])

    return (
        <Tippy className='popup' content={
            <span>
                {effectsData.loading && 'loading...'}
                {effectsData.error && effectsData.error.response.data.detail}
                {effectsData.result && effectsData.result.map(ingredient => {
                    return(
                        <div>
                            {`מרכיבים: ${ingredient.materials.join(', ')}`}
                            <br />
                            {`טכניקה: ${ingredient.technic}`}
                        </div>
                    )
                })}
            </span>
            }>
            <div className='tag'>{props.effect}</div>
        </Tippy>
    )
}


export { PotionDeleter, EffectTag }