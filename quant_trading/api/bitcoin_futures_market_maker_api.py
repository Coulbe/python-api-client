# coding: utf-8

"""
    Quant Trading Network API

    This API will use JSON.         JSON looks like this:                {         \"key\": \"value\",         \"anotherKey\": \"anotherValue\"       }  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: support@quant-trading.network
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from quant_trading.api_client import ApiClient


class BitcoinFuturesMarketMakerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_algo_params(self, **kwargs):  # noqa: E501
        """get_algo_params  # noqa: E501

        Get algorithm parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_algo_params(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AlgoParamsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_algo_params_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_algo_params_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_algo_params_with_http_info(self, **kwargs):  # noqa: E501
        """get_algo_params  # noqa: E501

        Get algorithm parameters  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_algo_params_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: AlgoParamsResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_algo_params" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/bitcoinFuturesMm/algo-params', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AlgoParamsResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_exec_algo(self, body, **kwargs):  # noqa: E501
        """post_exec_algo  # noqa: E501

        Determine algorithm execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_exec_algo(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExecPositionManagerAlgoRequest body: A JSON object containing the current position manager algorithm information. (required)
        :return: ExecAlgoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.post_exec_algo_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.post_exec_algo_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def post_exec_algo_with_http_info(self, body, **kwargs):  # noqa: E501
        """post_exec_algo  # noqa: E501

        Determine algorithm execution  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_exec_algo_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ExecPositionManagerAlgoRequest body: A JSON object containing the current position manager algorithm information. (required)
        :return: ExecAlgoResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_exec_algo" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `post_exec_algo`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['ApiKeyAuth']  # noqa: E501

        return self.api_client.call_api(
            '/bitcoinFuturesMm/exec-algo', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ExecAlgoResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)