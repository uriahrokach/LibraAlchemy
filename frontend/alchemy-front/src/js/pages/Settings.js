import React, {useState} from 'react';
import { LabeledElement } from '../components/SearchComponents';

const Settings = (props) => {
    return (
        <div>
            <h3>potion settings</h3>
            <LabeledElement label='Maximum number of elements:'>
                <input type='number'/>
            </LabeledElement>
            <LabeledElement label='Materials'>
                <input type='file' />
            </LabeledElement>
        </div>
    );
}

export {Settings};