import React, { useState, useEffect} from "react";
import { faUserEdit,faUserMinus} from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import './App.css';
import api from './axiosinstance';
import  Bootbox  from  'bootbox-react';

export default function Client({value}) {
    const [showConfirm,setShowConfirm] = useState(false)
    /**
     * Método responsavel por excluir o usuário.
     */
    const deleteSubmit = () =>{
        api.delete('/pessoa/'+value.id)
        .then((data) => {
          return data.data;
        }).then(data => {

        })
    }

    const handleNo = () => {
        setShowConfirm(false)
    }

    return (
        <tr>                      
            <td>{value.id}</td>
            <td>{value.nome}</td>
            <td>{value.cpf}</td>
            <td>{value.data_nascimento}</td>
            <td>{value.logradouro}, {value.numero} - {value.bairro} - {value.cidade} - {value.estado}, {value.cep} - {value.pais}</td>
            <td><button className="btn btn-primary btn-icon-only" style={{float:'right',fontSize:11}}><FontAwesomeIcon icon={faUserEdit} /></button></td>
            <td><button className="btn btn-danger btn-icon-only" style={{float:'right',fontSize:11}}><FontAwesomeIcon onClick={() => setShowConfirm(true)} icon={faUserMinus} /></button></td>
        
            <Bootbox show={showConfirm} 
				type={"confirm"}  
				message={"Do That?"}  
				onSuccess={deleteSubmit}  
				onCancel={handleNo}  
				onClose={handleNo} 
			/>
        </tr>
    )
}