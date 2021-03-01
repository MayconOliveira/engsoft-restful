import React, { useState, useEffect} from "react";
import logo from './logo.svg';
import './App.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faUserEdit,faUserMinus,faUserPlus } from '@fortawesome/free-solid-svg-icons'
import 'bootstrap/dist/css/bootstrap.min.css';
import api from './axiosinstance';
import Client from "./client";

function App() {
  const [state,setState] = useState([]);


  useEffect(() => {
    load()
  });

  /**
   * Métodos responsável por buscar todas as pessoas e adicionar em um state.
   * @uses useEffect()
   */
  const load = () =>{
    api.get('/pessoas')
    .then((data) => {
      return data.data;
    }).then(data => {
      setState(data);
    })
  }

  return (
    <div className="main-content">
      <div className="container mt-5">   
        <h2 className="mb-5">CPF Busca</h2>
        <div className="row justify-content-md-center"> 
          <div className="col-md-6">
            <div className="form-group">
              <input type="text" name="busca" placeholder="Buscar por CPF" className="form-control" />
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
                    <button className="btn btn-success btn-icon-only" style={{float:'right',fontSize:11}}><FontAwesomeIcon icon={faUserPlus} /></button>
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
                            <Client value={value} key={index} />
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
    </div>
  );
}

export default App;
