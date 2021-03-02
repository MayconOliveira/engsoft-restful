import React, { useState, useEffect} from "react";
import { faUserEdit,faUserMinus} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './App.css';
import api from './axiosinstance';
import  Bootbox  from  'bootbox-react';

export default function Form({value,load}) {



    return(
        <div className="row">
            <div class="col-md-4 mb-3">
                <label for="exampleFormControlInput1" class="form-label">Pais</label>
                <input type="email" class="form-control" id="exampleFormControlInput1" />
            </div>
            <div class="col-md-4 mb-3">
                <label for="exampleFormControlInput1" class="form-label">Estado</label>
                <input type="email" class="form-control" id="exampleFormControlInput1" />
            </div>
            <div class="col-md-4 mb-3">
                <label for="exampleFormControlInput1" class="form-label">Cidade</label>
                <input type="email" class="form-control" id="exampleFormControlInput1" />
            </div>
            <div class="col-md-4 mb-3">
                <label for="exampleFormControlInput1" class="form-label">Bairro</label>
                <input type="email" class="form-control" id="exampleFormControlInput1" />
            </div>
            <div class="col-md-5 mb-3">
                <label for="exampleFormControlInput1" class="form-label">Logradouro</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" />
            </div>
            <div class="col-md-3 mb-3">
                <label for="exampleFormControlInput1" class="form-label">Número</label>
                <input type="number" class="form-control" id="exampleFormControlInput1" />
            </div>
            <div class="col-md-12 mb-3">
                <label for="exampleFormControlInput1" class="form-label">Complemento</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" />
            </div>
            <div class="col-md-12 mb-3">
                <label for="exampleFormControlInput1" class="form-label">Nome</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" />
            </div>
            <div class="col-md-6 mb-3">
                <label for="exampleFormControlInput1" class="form-label">CPF</label>
                <input type="text" class="form-control" id="exampleFormControlInput1" />
            </div>
            <div class="col-md-6 mb-3">
                <label for="exampleFormControlInput1" class="form-label">Data de Nascimento</label>
                <input type="date" class="form-control" id="exampleFormControlInput1" />
            </div>
        </div>
    )
}