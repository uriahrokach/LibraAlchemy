import React, { useState, useEffect } from 'react';
import { useAsync } from 'react-async-hook';

import {DynamicMultipleChoice, DynamicRadioList} from '../components/SearchComponents'; 
import { getMaterials, getTechnics, brewPotions, getEffects } from '../utils/ServerUtils';
import PotionTable from '../components/PotionTable';
import { EffectTag } from '../components/PotionComponents';


import '../../css/Alchemist.css';
import '../../css/PotionComps.css'

const Alchemist = () => {
  const [materials, setMaterials] = useState([]);
  const [technic, setTechnic] = useState('');

  return (
    <div>
      <FormPage materials={materials} setMaterials={setMaterials} technic={technic} setTechnic={setTechnic}/>
      <PotionsPage materials={materials} technic={technic}/>
    </div>
  );
}

const FormPage = ({materials, setMaterials, technic, setTechnic}) => {
  const asyncMaterials = useAsync(getMaterials, []);
  const asyncTechnics = useAsync(getTechnics, []);

  return (
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
  );
}


const MaterialPage = ({items, results, setResults}) => {
  return (
    <div className='list-card'>
      <h3>רכיבים</h3>
      <DynamicMultipleChoice choices={items} results={results} setResults={(item) => {
        if (results.includes(item)){
          setResults(results.filter(key => key !== item));
        } else {
          setResults([...results, item]);
        }
      }}/>
      <button className='normal-button' onClick={() => setResults([])}>נקה</button>
    </div>
  );
}

const TechnicPage = ({items, technic, setTechnic}) => {
  return (
    <div className='list-card'>
      <h3>טכניקות</h3>
      <DynamicRadioList choices={items} result={technic} name='technics' setResults={setTechnic}/>
      <button className='normal-button' onClick={() => setTechnic('')}>נקה</button>
    </div>
  );
}

const PotionsPage = ({materials, technic}) => {
  const asyncPotion = useAsync(brewPotions, [materials, technic]);
  const asyncEffects = useAsync(getEffects, [materials, technic]);

  return (
    <div>
      {asyncEffects.error && asyncEffects.error.response.status != 400 && <div> {`error: ${asyncEffects.error.response.data.detail}\n`} </div>}
      {asyncEffects.result && (<div>{asyncEffects.result.map(effect => <EffectTag effect={effect.name} />)}</div>)}

      {asyncPotion.error && asyncPotion.error.response.status != 400 && <div> {`error: ${asyncPotion.error.response.data.detail}\n`} </div>}
      {asyncPotion.result && (
        <div>
          <PotionTable potions={asyncPotion.result} deletePotion/>
        </div>
      )}
      {asyncEffects.loading && asyncPotion.loading && "loading..."}

    </div>
  );
}

export default Alchemist;
export {MaterialPage, TechnicPage};
