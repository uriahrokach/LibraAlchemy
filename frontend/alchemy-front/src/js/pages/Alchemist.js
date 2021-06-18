import React, { useState } from 'react';
import {ListBarController, DynamicMultipleChoice, DynamicRadioList} from '../components/SearchComponents'; 
import {getMaterials, getTechnics, brewPotions} from '../utils/ServerUtils';
import PotionTable from '../components/PotionTable';
import { useAsync } from 'react-async-hook';

import '../../css/Alchemist.css';

const Alchemist = () => {
  const [materials, setMaterials] = useState([]);
  const [technic, setTechnic] = useState('');

  const [submit, setSubmit] = useState(false)

  return (
    <div>
      <FormPage setSubmit={setSubmit} materials={materials} setMaterials={setMaterials} technic={technic} setTechnic={setTechnic}/>
      {submit && <PotionsPage materials={materials} technic={technic} setSubmit={setSubmit}/>}
    </div>
  );
}

const FormPage = ({setSubmit, materials, setMaterials, technic, setTechnic}) => {
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
          <button onClick={() => setSubmit(true)}>Brew Potion</button>
        </div>
      )}
    </div>
  );
}


const MaterialPage = ({items, results, setResults}) => {
  const [matChoices, setMatChoices] = useState(items);

  return (
    <div className='list-card'>
      <ListBarController items={items} setChoices={setMatChoices}/>
      <DynamicMultipleChoice choices={matChoices} setResults={(item) => {
        if (results.includes(item)){
          setResults(results.filter(key => key !== item));
        } else {
          setResults([...results, item]);
        }
      }}/>
      <button onClick={() => setResults([])}>Clean</button>
      <h3>{results.toString()}</h3>
    </div>
  );
}

const TechnicPage = ({items, technic, setTechnic}) => {
  const [tecChoices, setTecChoices] = useState(items);
  
  return (
    <div className='list-card'>
      <ListBarController items={items} setChoices={setTecChoices}/>
      <DynamicRadioList choices={tecChoices} name='technics' setResults={setTechnic}/>
      <button onClick={() => setTechnic('')}>Clean</button>
      <h3>{technic}</h3>
    </div>
  );
}

const PotionsPage = ({materials, technic}) => {
  const asyncPotion = useAsync(brewPotions, [materials, technic]);

  return (
    <div>
      {asyncPotion.loading && "loading..."}
      {asyncPotion.error && `error: ${asyncPotion.error.message}, ${asyncPotion.error.data}`}
      {asyncPotion.result && (
        <div>
          <PotionTable potions={asyncPotion.result}/>
        </div>
      )}
    </div>
  );
}

export default Alchemist;
