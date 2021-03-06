import React, { Component } from 'react';
import {
    Link
} from 'react-router-dom';
import PropTypes from 'prop-types';

import {
    Col,
    Card
} from 'antd';

import {
    FULL_QUIZZES_PATH
} from './../../../routes';

class RegisterFullQuizzesElement extends Component {
    render () {
        const {
            quiz
        } = this.props;
        
        return (
            <Col style={{ width: '25%' }}>
                <Card>
                    <Link to={`${FULL_QUIZZES_PATH}/topic/${quiz.id}`}>
                        <div
                            style={{
                                display: 'flex',
                                justifyContent: 'space-between',
                                alignItems: 'center'
                            }}
                        >
                            <div>
                                {quiz.name}
                            </div>
                        </div>
                    </Link>
                </Card>
            </Col>   
        );
    }
}

RegisterFullQuizzesElement.propTypes = {
    quiz: PropTypes.objectOf(PropTypes.any).isRequired
};

export default RegisterFullQuizzesElement;
