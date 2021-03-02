import React, { useState, useEffect} from "react";
import { faUserEdit,faUserMinus} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './App.css';
import api from './axiosinstance';
import Modal from 'react-bootstrap4-modal';
import Form from "./Form";

export default function Client({value,load}) {
    const [showConfirm,setShowConfirm] = useState(false);
    const [modal,setModal] = useState(false);
    
    useEffect(() => {
        
    },[setShowConfirm]);

    /**
     * Método responsavel por excluir o usuário.
     */
    const deleteSubmit = () =>{
        api.delete('/pessoas/'+value.id)
        .then((data) => {
          return data.data;
        }).then(data => {
            load();
        })
    }

    const handleNo = () => {
        setShowConfirm(false)
    }

    return (
        <tr>                      
            <td>{value.id}</td>
            <td>{value.nome_pessoa}</td>
            <td>{value.cpf}</td>
            <td>{value.data_nascimento}</td>
            <td>{value.logradouro}, {value.numero} - {value.bairro_nome} <br/><small style={{fontSize:11,color:'#bb9f9f'}}>{value.cidade_nome} - {value.estado_nome}, {value.cep} - {value.pais_nome}</small></td>
            <td><button className="btn btn-primary btn-icon-only" style={{float:'right',fontSize:11}} onClick={() => setModal(true)}><FontAwesomeIcon icon={faUserEdit} /></button></td>
            <td><button className="btn btn-danger btn-icon-only" style={{float:'right',fontSize:11}} onClick={() => {if(window.confirm('Deseja excluir a pessoa '+value.nome_pessoa)) deleteSubmit() } }><FontAwesomeIcon  icon={faUserMinus} /></button></td>
            <Modal visible={modal} >
                <div className="modal-header">
                    <h5 className="modal-title">Edição</h5>
                </div>
                <div className="modal-body">
                    <Form />
                </div>
                <div className="modal-footer">
                <button type="button" className="btn btn-secondary" onClick={() => setModal(false)}>
                    Cancelar
                </button>
                <button type="button" className="btn btn-primary" >
                    Salvar
                </button>
                </div>
            </Modal>
        </tr>
    )
}