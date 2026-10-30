def test_failurespot_complete_smoke(tmp_path):
    from failurespot.smoke import run_smoke

    result = run_smoke(tmp_path)
    assert result["mlp"]["selected_count"] == 23
    assert result["lstm"]["selected_count"] == 23
    assert result["weak_random_finetune_mlp"]["selected_count"] == 23
    assert result["trajectory_active_finetune_lstm"]["selected_count"] == 23
    assert result["safe_mlp"]["selected_count"] == 0
    assert result["supervised_random_lstm"]["selected_count"] == 23
    assert result["stac"]["applicable"] is True
    assert result["logpzo"]["architecture"] == "flow_unet"
