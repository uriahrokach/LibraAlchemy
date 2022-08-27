import React, {useState} from 'react';

import ReactDOM from 'react-dom';
import { useAsync } from 'react-async-hook';
import { toast } from 'react-toastify';
import Tippy from '@tippy.js/react';

import { InputController, TextAreaController } from './SearchComponents';
import { deletePotion, getEffectByName, createPotion, getEffects } from '../utils/ServerUtils';

import '../../css/PotionComps.css';
import 'tippy.js/dist/tippy.css';

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

const PotionMaker = (props) => {
    const [name, setName] = useState('');
    const [desc, setDesc] = useState('');
    const asyncEffects = useAsync(getEffects, [props.materials, props.technic]);

    return (
        <Modal>
            <h3>יצירת שיקוי</h3>
            {asyncEffects.error && asyncEffects.error.response.status != 400 && <div> {`error: ${asyncEffects.error.response.data.detail}\n`} </div>}
            {asyncEffects.result && (<div>{asyncEffects.result.map(effect => <EffectTag effect={effect.name} />)}</div>)}
            
            <InputController setValue={setName} placeholder='שם השיקוי...' />
            <TextAreaController setValue={setDesc} placeholder='תיאור...' />

            <div>
                <button className='alert-button' onClick={async () => {
                    try{
                        const response = await createPotion(name, props.materials, props.technic, desc);
                        toast.success(response);
                        props.setActive(false);
                    } catch (error) {
                        toast.error(error.response.data.detail);
                    }
                } }>צור שיקוי</button>
                <button className='normal-button' onClick={() => { props.setActive(null) }}>ביטול</button>
            </div>
        </Modal>
    )
}

const EffectTag = (props) => {
    const effectsData = useAsync(getEffectByName, [props.effect]);

    return (
        <Tippy className='popup' content={
            <span>
                {effectsData.loading && 'loading...'}
                {effectsData.error && effectsData.error.response.data.detail}
                {effectsData.result && effectsData.result.reactions.map(ingredient => {
                    return(
                        <div className='popup-div'>
                            {`מרכיבים: ${ingredient.materials.join(', ')}`}
                            <br />
                            {`טכניקה: ${ingredient.technic}`}
                        </div>
                    )
                })}
                {effectsData.result && effectsData.result.enhance && <div className='popup-enhance'><b>אפקט מיוחד: {effectsData.result.enhanceDescription}</b></div>}
            </span>
            }>
            <div className={ effectsData.result && effectsData.result.enhance ? 'enhance-tag' : 'tag' }>{props.effect}</div>
        </Tippy>
    )
}



const PotionTypeTag = (props) => {
    return (
        <Tippy className='popup' content={
            <span>
                <div>תיאור: {props.description}</div>
                <div>{props.effects.map(effect => effect.name).join(', ')}</div>
            </span>
        }>
            <div className="tag">{props.name}</div>
        </Tippy>
    )
}

export { PotionDeleter, EffectTag, PotionMaker, PotionTypeTag }