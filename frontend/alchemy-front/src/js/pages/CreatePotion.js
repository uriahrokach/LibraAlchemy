import React, {useState} from 'react';
import { useAsync } from 'react-async-hook';
import { toast } from 'react-toastify';

import { MaterialPage, TechnicPage } from './Alchemist';
import { EffectTag } from '../components/PotionComponents';
import { InputController, TextAreaController } from '../components/SearchComponents';
import {getMaterials, getTechnics, getEffects, createPotion} from '../utils/ServerUtils';

import '../../css/PotionComps.css';
import '../../css/CreatePotion.css';

const potionMake = async (name, materials, technic, description) => {
    try {
        const result = await createPotion(name, materials, technic, description);
        toast.success(result);
    } catch (error) {
        toast.error(error.response.data.detail);
    }

}

const CreatePotion = () => {
    const [name, setName] = useState('');
    const [materials, setMaterials] = useState([]);
    const [technic, setTechnic] = useState('');
    const [desc, setDesc] = useState('');

    const asyncMaterials = useAsync(getMaterials, []);
    const asyncTechnics = useAsync(getTechnics, []);
    const asyncEffects = useAsync(getEffects, [materials, technic]);
  
    return (
      <div>
        <div className='create-potion'>
            <div className='input-div'>
                <InputController setValue={setName} placeholder='שם השיקוי...' />
                <TextAreaController setValue={setDesc} placeholder='תיאור...' />
                {asyncEffects.error && asyncEffects.error.response.status != 400 && <div> {`error: ${asyncEffects.error.response.data.detail}\n`} </div>}
                {asyncEffects.result && <div>אפקטים:</div>}
                <br/>
                {asyncEffects.result && (<div>{asyncEffects.result.map(effect => <EffectTag effect={effect.name} />)}</div>)}
                {asyncEffects.loading && "loading..."}
                <br />
                <button className='normal-button' onClick={() => potionMake(name, materials, technic, desc)}>צור שיקוי</button>
            </div>
            <div>
                {asyncMaterials.loading || asyncTechnics.loading && <p>Loading...</p>}
                {asyncMaterials.error && <p>{`error: ${asyncMaterials.error.stack}`}</p>}
                {asyncTechnics.error && <p>{`error: ${asyncTechnics.error.message}`}</p>}
                {asyncMaterials.result && asyncTechnics.result && (
                    <div>
                        <div className='alchemy'>
                        <MaterialPage items={asyncMaterials.result} results={materials} setResults={setMaterials}/>
                        <TechnicPage items={asyncTechnics.result} technic={technic} setTechnic={setTechnic}/>
                        </div>
                    </div>
                )}
            </div>
        </div>
      </div>
    );
  }

export { CreatePotion };