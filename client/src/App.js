import React, { useState, useEffect} from "react";
import logo from './logo.svg';
import './App.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserEdit,faUserMinus,faUserPlus } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css';
import api from './axiosinstance';
import Client from "./Client";
import Modal from 'react-bootstrap4-modal';
import Form from "./Form";

function App() {
  const [state,setState] = useState([]);
  const [modal,setModal] = useState(false);

  useEffect(() => {
    load()
  },[]);

  /**
   * Métodos responsável por buscar todas as pessoas e adicionar em um state.
   * @uses useEffect()
   */
  const load = () =>{
    api.get('/pessoas')
    .then((data) => {
      return data.data;
    }).then(data => {
      setState(data.pessoas);
    })
  }

  /**
   * Método responsável por buscar a pessoa pelo número do CPF
   * @param {*} e 
   */
  const getPessoa = (e) => {   
    if(e.target.value.length > 0 ) {
      api.get('/pessoas/'+e.target.value)
      .then((data) => {
        return data.data;
      }).then(data => {
        setState(data.pessoa);
      })
    }else{
      load()
    }
  }

  /**
   * Retorno da aplicação.
   */
  return (
    <div className="main-content">
      <div className="container mt-5">   
        <h2 className="mb-5">CPF Busca</h2>
        <div className="row justify-content-md-center"> 
          <div className="col-md-6">
            <div className="form-group">
              <input type="text" name="busca" onChange={getPessoa} placeholder="Buscar por CPF" className="form-control" />
            </div>
          </div>          
        </div>
        <div className="row mt-5">
          <div className="col">
            <div className="card shadow">
              <div className="card-header border-0">
                <div className="row">
                  <div className="col-md-6">
                    <h5 className="mt-1">Pessoas</h5>
                  </div>
                  <div className="col-md-6">
                    <button className="btn btn-success btn-icon-only" style={{float:'right',fontSize:11}} onClick={() => setModal(true)}><FontAwesomeIcon icon={faUserPlus} /></button>
                  </div>
                </div>                
              </div>
              <div className="table-responsive">
                {state.length > 0 ? 
                  <table className="table align-items-center table-flush">
                    <thead className="thead-light">
                      <tr>                      
                        <th scope="col">ID</th>
                        <th scope="col">Nome</th>
                        <th scope="col">CPF</th>
                        <th scope="col">Data de Nascimento</th>
                        <th scope="col">Endereço</th>
                        <th scope="col"></th>
                        <th scope="col"></th>
                      </tr>
                    </thead>
                    <tbody>
                      {
                        state.map((value,index) =>{
                          return (
                            <Client value={value} load={load} key={index} />
                          )
                        })
                      }
                    </tbody>
                  </table>
                :
                  <div style={{textAlign:'center',margin:40}}>Nenhuma pessoa encontrada...</div>
                }
              </div>
            </div>
          </div>
        </div>
      </div>
      <Modal visible={modal} >
        <div className="modal-header">
          <h5 className="modal-title">Cadastro</h5>
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
    </div>
  );
}

export default App;
